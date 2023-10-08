FROM public.ecr.aws/lambda/python:3.11

RUN yum install -y \
    Xvfb \
    wget \
    unzip

# Install google-chrome-stable
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
    yum localinstall -y google-chrome-stable_current_x86_64.rpm

# Install chromedriver
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.149/linux64/chromedriver-linux64.zip && \
    unzip -j chromedriver-linux64.zip && \
    chmod 775 chromedriver

COPY . ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements.txt --no-cache-dir

CMD [ "lambda_function.handler" ]