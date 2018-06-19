FROM openjdk:8-jdk-alpine

COPY resources /getpid/
RUN cd /getpid && javac RunJython.java
# CMD cd /getpid && java -classpath .:jython-standalone-2.7.1.patch2618.jar RunJython
CMD cd /getpid && java -jar jython-standalone-2.7.1.jar getpid.py
