FROM node:alpine
COPY cli.js /cli.js
COPY lib /lib
ENTRYPOINT ["node", "cli.js"]