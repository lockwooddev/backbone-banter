"use strict";


define([
    'underscore',
    'backbone'
], function(_, Backbone){

    var ThreadModel = Backbone.Model.extend({

        defaults: {
            com: "com"
        }
    });

    return ThreadModel;
});