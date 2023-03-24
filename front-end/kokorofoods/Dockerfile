FROM node:15.9.0

RUN mkdir -p /home/kokorofoods/front-end
WORKDIR /home/kokorofoods/front-end

# COPY package.json /home/kokorofoods/front-end
# update and install dependency
# RUN apk update && apk upgrade

EXPOSE 3000
ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

COPY . /home/kokorofoods/front-end
RUN chmod -R 777 /home/kokorofoods/front-end
# RUN rm -rf node_modules/ package-lock.json
RUN npm install
#RUN npm install
# RUN npm install -g npm@7.21.0
# RUN rm -rf /home/kokorofoods/front-end/node_modules/npm
# RUN mv node_modules/npm /home/kokorofoods/front-end/node_modules/npm
# RUN npm install
RUN npm run build
# expose 5000 on container


# start the app
CMD npm start
# CMD npm start
# RUN npm ci --only=production

# # Bundle app source
# COPY . .

# EXPOSE 3000
# CMD [ "node", "server.js" ]