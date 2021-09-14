# Versão do pip
python -m pip --version

# Install upgrade
python -m pip install --upgrade sampleproject
pip install --upgrade sampleproject

# Desintalando pacotes
python -m pip uninstall sampleproject
pip uninstall sampleproject

# Listando pacotes
pip show <packagename>
pip freeze

# Criando arquivo requirements com os pacotes instalados
pip freeze --all > requirements.txt
python -m pip freeze > requirements.txt

# Listando os pacotes e suas versões
!pip freeze

# Instalando uma lista de pacotes no pip
python -m pip install -r requirements.txt
pip install -r requirements.txt

# Desisntando todos os pacotes no pip
 pip uninstall -y (pip freeze)
 pip uninstall -y -r requirements.txt 

 # Documentação pip 
 https://pip.pypa.io/en/stable/installation/