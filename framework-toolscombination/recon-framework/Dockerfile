FROM kalilinux/kali-rolling

# Install reconnaissance tools
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    nmap \
    dnsutils \
    theHarvester \
    amass \
    gobuster \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /recon-framework

# Copy framework files
COPY . /recon-framework

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Create output directory
RUN mkdir -p output

# Set permissions
RUN chmod +x main.py examples.py report_generator.py

# Default command
ENTRYPOINT ["python3", "main.py"]
