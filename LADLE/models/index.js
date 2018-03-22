// ./models/index.js
const Sequelize = require('sequelize');
const config = require('../config.json');
const fs = require('fs');
const path = require('path');

const sequelize = new Sequelize(
    config.database,
    config.username,
    config.password,
    {
        host: config.hostname,
        dialect: 'postgres'
    }
);
const db = {};

// models配下のjsファイルを読み込む
fs.readdirSync(__dirname)
    .filter(file => file.indexOf('.js') && file !== 'index.js')
    .forEach(file => {
        const model = sequelize.import(path.join(__dirname, file));
        db[model.name] = model;
    });

// 今回はassociateの定義をしないので実行されない
Object.keys(db).forEach(modelName => {
    if ('associate' in db[modelName]) {
        db[modelName].associate(db);
    }
});

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;