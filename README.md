# gemma-web-service
A simple implementation of a Gemma web service using Python.

### Install the prerequisites

This project uses Python 3 and Python Poetry to manage packages and
run the application. The following installation instructions are for a Linux
host machine.

To install the required software:

1.  Install Python 3 and the `venv` virtual environment package for Python.
<pre>
sudo apt update
sudo apt install git pip python3-venv
</pre>

### Clone and configure the project

Download the project code and use the setup.sh command to download
the required dependencies and configure the project. You need
[git](https://git-scm.com/) source control software to retrieve the
project source code.

To download and configure the project code:

1.  Clone the git repository using the following command.
<pre>
git clone https://github.com/joefernandez/gemma-web-service.git
</pre>
1.  Move to the `gemma-web-service` project root directory.
<pre>
cd gemma-web-service
</pre>
1.  Run the `installation.sh` script to create a Python virtual environment
    `venv` and directory, or run the following command: 
<pre>
python3 -m venv venv
</pre>
1.  Activate the Python virtual environment, and make sure `(venv)` appears
    at the begin