FROM python:3.9

#Setting the working directory
WORKDIR /usr/src/app

#Copying the requirements file into the working directory
COPY requirements.txt ./

#Installing all of the dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#Copying the rest of the bot's code
COPY . . 

#Allowing different traffic on different ports
EXPOSE 8080

#Running the bot
CMD ["python", "C:\Users\megan\OneDrive\Documents\Project\cbb\Character-Birthday-Bot\main.py"]
