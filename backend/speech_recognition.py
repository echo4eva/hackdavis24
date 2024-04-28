import torch
from transformers import pipeline
from datasets import load_dataset

def main():
  device = "cuda:0" if torch.cuda.is_available() else "cpu"

  pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny",
    chunk_length_s=30,
    device=device,
  )

  # ds = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation")
  sample = "output.wav"

  prediction = pipe(sample, batch_size=8)["text"]

  # we can also return timestamps for the predictions
  # prediction = pipe(sample.copy(), batch_size=8, return_timestamps=True)["chunks"]
  return prediction

if __name__ == "__main__":
    main()