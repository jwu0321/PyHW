git config --global user.name 'jwu0321'
git config --global user.email 'jwu271@binghamton.edu'

git pull --unshallow

git remote add upstream https://github.com/wusimon51/PyHW.git
git fetch upstream

git merge --no-edit upstream/main
git push origin main