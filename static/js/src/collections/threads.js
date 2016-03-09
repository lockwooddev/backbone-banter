"use strict";


define([
    'underscore',
    'backbone',
    'models/thread'
], function(_, Backbone, ThreadModel){

    var ThreadCollection = Backbone.Collection.extend({
        model: ThreadModel,

        url: function(board){
            return 'api/boards/'+ board + '/catalog'
        },

        parse: function(resp, xhr) {

            var unpacked = [];

            for (var pageId = 0; pageId <= resp.length - 1; pageId += 1) {

                var threadPage = resp[pageId];

                for (var i = 0; i <= threadPage.threads.length - 1; i += 1) {
                    // console.log(threadPage.threads[i]);
                    unpacked.push(threadPage.threads[i]);
                }
            }

            return unpacked;
        },
    });

    return ThreadCollection;
});