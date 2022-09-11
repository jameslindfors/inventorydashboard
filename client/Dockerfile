FROM node:18.9-slim AS build

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

FROM node:buster-slim AS deploy-node

WORKDIR /app
RUN rm -rf ./*
COPY --from=build /app/package.json .
COPY --from=build /app/build .
RUN npm i --omit=dev

CMD [ "node", "index.js" ]