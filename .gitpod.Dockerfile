# Install pipx
RUN echo "WTF"
RUN python -m pip install pipx
RUN pipx ensurepath

# Install algokit
RUN pipx install algokit