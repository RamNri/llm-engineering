import time

from openai import (APIConnectionError, APITimeoutError, RateLimitError)

def get_retry_delay(error, attempt, initial_delay,):
  """
  Determine how long to wait before retrying.

  priority:
  1. Use server-provided Retry-After value when available.
  2. Otherwise use exponential backoff.
  """

  response = getattr(error, "response", None)
  if response:
    retry_after = response.headers.get("retry-after")
    if retry_after:
      try:
        return float(retry_after)
      except ValueError:
        pass

  return initial_delay * (2 ** attempt)

def call_llm_with_retry(operation, max_attempts= 3, initial_delay = 5):
  """
  Call an OpenAI-compatible LLM API with basic retry handling

  Retries temporary failures such as
   -Rate Limits
   -Timeouts
   -Connection errors
  """

  for attempt in range(max_attempts):
    try:

      print(
        f"\nAttempt "
        f"(attempt {attempt + 1}/{max_attempts})..."
      )

      response = operation()
      print("Request Successful")

      return response

    except (
      RateLimitError,
      APITimeoutError,
      APIConnectionError) as error:

      print(f"\n Attempt {attempt + 1} failed")
      print(f"\n ---Error Details---")
      print(f"Error type: {type(error)}")
      print(f"Error message: {error}")
      print(f"Response:"
            f"{getattr(error, 'response', None)}")

      #if this ws the final attempt do not wait unnessarily

      if attempt == max_attempts - 1:
        break

      delay = get_retry_delay(
        error, attempt, initial_delay,
      )

      print(
        f"Retrying in {delay} seconds..."

      )

      time.sleep(delay)

  raise RuntimeError(
    f"Operation failed after {max_attempts} attempts"
  )     