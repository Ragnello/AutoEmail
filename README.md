# AutoEmail
Projeto de automação de identificação e classificação de emails no Google Drive.

## Etapas do projeto

* Criação da estrutura básica do projeto
* Criação as credenciais e vínculo das credenciais com o código principal
* Padronização e limpeza das informações
* Pesquisa de armazenamento das informações
* Teste de armazenamento das informações no Google Drive
* Concluir projeto

## Estrutura de Pastas

```txt
AutoEmail
├── main.py
├── info.py
├── README.md
├── .gitignore
```

## Comandos de atualização do repositório

Para atualizar o repositório Github, basta ter o Git instalado e seguir os seguintes passos:

  1. Certifique-se que você está na branch desejada -> `git branch nomedabranch`
  2. Atualize a branch principal do projeto -> `git pull origin main`
  3. Mescle as mudanças da branch de desenvolvimento na branch principal -> `git checkout main` e em seguida `git merge nomedabranch`
  4. Verifique se os arquivos já estão prontos para o commit -> `git status` (Se estiverem vermelhos, continuar no passo 5. Se estiverem verdes, pular para o passo 6.)
  5. Adicione todas as mudanças -> `git add .`
  6. Commit das mudanças -> `git commit -m "Mensagem de integração das mudanças"`
  7. Atualize o repositório Github -> `git push origin main`
  
(OPCIONAL) Caso não vá utilizar mais a branch, poderá excluí-la com os seguintes comandos:
* Excluir localmente -> `git branch -d nomedabranch`
* Excluir remotamente -> `git push origin --delete nomedabranch`