#
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import re
from dotenv import load_dotenv

# Set the backbend before importing Keras
os.environ["KERAS_BACKEND"] = "jax"
# Avoid memory fragmentation on JAX backend.
os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"] = "1.00"

import keras_nlp

os.environ["KERAS_BACKEND"] = "jax"  # Or "tensorflow" or "torch".
os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"] = "0.9"

def initialize_model():
    """Loads environment variables and configures the Gemma model."""
    load_dotenv()
    kaggle_username = os.getenv('KAGGLE_USERNAME')
    if not kaggle_username:
        raise ValueError("KAGGLE_USERNAME environment variable not found. Did you set it in your .env file?")
    kaggle_key = os.getenv('KAGGLE_KEY')
    if not kaggle_key:
        raise ValueError("KAGGLE_KEY environment variable not found. Did you set it in your .env file?")

    # create instance using Gemma 2 2B instruction tuned model
    gemma = keras_nlp.models.GemmaCausalLM.from_preset("gemma2_instruct_2b_en")
    #gemma.summary() # REMOVE: FOR TESTING ONLY
    return gemma  # Return the initialized model

def create_message_processor():
    """Creates a message processor function with a persistent model."""
    model = initialize_model()

    def process_message(prompt_text):
        """Processes a message using a local Gemma model."""
        input = f"<start_of_turn>user\n{prompt_text}<end_of_turn>\n<start_of_turn>model\n"
        response = model.generate(input, max_length=512)
        # remove response tags
        response = trim_response(input, response)

        print(response) # REMOVE: FOR TESTING ONLY
        return response

    return process_message

def trim_response(prefix, response_text):
  """
  Removes prompt prefix "<end_of_turn>\n<start_of_turn>model..." and suffix "<end_of_turn>".
  Args:
      text: The response text.
  Returns:
      The trimmed substring, or original if string prefix and suffix are not found.
  """
  # remove the prompt prefix and suffix
  response_text = response_text.removeprefix(prefix)
  response_text = response_text.removesuffix("<end_of_turn>")
  return response_text

# default method
if __name__ == "__main__":
    process_message = create_message_processor()
    process_message("roses are red")
    #print(extract_substring("<start_of_turn>user\nTHE PROMPT<end_of_turn>\n<start_of_turn>model\nTHE TEXT RESPONSE"))
