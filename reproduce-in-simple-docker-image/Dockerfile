FROM openjdk:8-jdk-alpine

COPY resources /jythonssl/
RUN cd /jythonssl && javac RunJython.java
CMD cd /jythonssl && java -classpath .:jython-standalone-2.7.1.patch2618.jar RunJython
