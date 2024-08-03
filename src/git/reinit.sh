# eval $(ssh-agent)
# ssh-add /home/tp/.ssh/id_rsa
rm -rf .git
git init
git add .
git remote add origin https://github.com/Phovos/quine.git
git commit -m "Initial commit"
git branch -m master quine
git push -u origin quine