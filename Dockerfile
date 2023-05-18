FROM python:latest

#it will copy req.txt and all py files into app directory.
copy requirement.txt  *.py  /app/

workdir /app

run pip install -r requirement.txt


CMD ["pytest"]

#to build an image
#docker build -t dockerimagename .
#check with command -->docker images to check if image was build
#next step
#docker run -p 4444:4444 dockerimagename

