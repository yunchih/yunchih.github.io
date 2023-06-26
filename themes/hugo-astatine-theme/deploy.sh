#!/bin/sh
#sh -c "cd public/static/ && [ -L static ] || ln -fs . static"
rsync -avqr  public/ /var/opt/yunchih/ --delete
