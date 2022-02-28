FROM python:3.11-rc-slim AS build-env
ADD . /app
WORKDIR /app

# Setting for publish
LABEL "com.github.actions.name"="File type finder action"
LABEL "com.github.actions.description"="Provides a list of paths and/or file names for specified files in folder/directory"

LABEL "repository"="https://github.com/ab185508/file-type-finder.git"
LABEL "homepage"="https://github.com/ab185508/file-type-finder.git"

# We are installing a dependency here directly into our app source dir
# RUN pip install --target=/app yamllint

# A distroless container image with Python and some basics like SSL certificates
# https://github.com/GoogleContainerTools/distroless
FROM gcr.io/distroless/python3
COPY --from=build-env /app /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["/app/main.py"]