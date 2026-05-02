FROM python:3.15.0a8-slim-bookworm

WORKDIR /app

RUN git clone https://github.com/yt-dlp/yt-dlp.git && \
    cd yt-dlp && python3 -m pip install pyinstaller && \
    python3 devscripts/install_deps.py --include-group pyinstaller && \
    python3 devscripts/make_lazy_extractors.py && \
    python3 -m bundle.pyinstaller

ENTRYPOINT ["yt-dlp", "-P /app/dls"]