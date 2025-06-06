#!/bin/bash

# Start Ollama server in the background
/bin/ollama serve &

# Wait for Ollama to be ready
echo "Waiting for Ollama server to start..."
while ! ollama list > /dev/null 2>&1; do
    sleep 2
done


echo "Ollama server is ready. Installing models..."

# Install DeepSeek model
echo "Installing DeepSeek R1 1.5B..."
ollama pull deepseek-r1:1.5b &

# Wait for all background downloads to complete
wait

echo "All models installed successfully!"
echo "Ollama is ready to use."

# Keep the server running
wait