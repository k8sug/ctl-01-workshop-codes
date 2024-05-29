
#Oficial Python runtime as a parent image
FROM python:3.8-slim                                                            
                                                                                
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir  flask  flask-cors transformers torch==2.2.2+cpu -f https://download.pytorch.org/whl/torch_stable.html

# Download the tokenizer and model
RUN python -c "from transformers import AutoTokenizer, AutoModelForSeq2SeqLM; \
               AutoTokenizer.from_pretrained('microsoft/GODEL-v1_1-base-seq2seq'); \
               AutoModelForSeq2SeqLM.from_pretrained('microsoft/GODEL-v1_1-base-seq2seq')"

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
