# eval $(ssh-agent)
# ssh-add /home/tp/.ssh/id_rsa
git add .
git commit -m "Initial commit"
eval $(ssh-agent)
ssh-add /home/tp/.ssh/id_rsa
git branch -m development # rename master to development
git remote set-url origin git@github.com:Phovos/quine.git # update SSH URL
git push origin HEAD:master