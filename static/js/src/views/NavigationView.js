"use strict";


define([
    'jquery',
    'underscore',
    'backbone',
    'collections/boards',
    'text!templates/boardNavTemplate.html',
    'views/ThreadListView',
], function($, _, Backbone, BoardCollection, boardNavTemplate, ThreadListView){

    var NavigationView = Backbone.View.extend({
        el: $('#nav'),

        events: {
            'click .board-nav': 'renderCatalog'
        },

        initialize: function(coll){
            this.coll = coll

            _.bindAll(this, 'render', 'renderCatalog');
        },

        render: function(){

            var data = {
                boards: this.coll.models,
                _: _
            };

            var compiledTemplate = _.template(boardNavTemplate);
            this.$el.append(compiledTemplate(data));
        },

        renderCatalog: function(el){
            // set active class for navigation
            $(el.currentTarget).parent().addClass('active');
            $(el.currentTarget).parent().siblings().removeClass('active');

            var targetArg = $(el.currentTarget).data('target');
            var threadListView = new ThreadListView(targetArg);
            threadListView.render();
        }
    });

    return NavigationView;
});