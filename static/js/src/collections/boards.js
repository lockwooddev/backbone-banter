"use strict";


define([
    'underscore',
    'backbone',
    'models/board'
], function(_, Backbone, BoardModel){

    var BoardCollection = Backbone.Collection.extend({
        model: BoardModel,
        url: 'api/boards/',
    });

    return BoardCollection;
});