"use strict";


define([
    'underscore',
    'backbone',
    'models/post'
], function(_, Backbone, PostModel){

    var PostCollection = Backbone.Collection.extend({
        model: PostModel,

        url: function(board, id){
            return 'api/boards/'+ board +'/threads/'+ id;
        },

        parse: function(resp, xhr) {
            return resp.posts
        }
    });

    return PostCollection;
});