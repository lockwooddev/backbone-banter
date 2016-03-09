"use strict";


define([
    'underscore',
    'backbone'
], function(_, Backbone){

    var PostModel = Backbone.Model.extend({

        defaults: {
            com: "com"
        }
    });

    return PostModel;
});