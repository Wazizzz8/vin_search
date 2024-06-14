odoo.define('add.kanban.view.buttons', function (require) {
    "use strict";

    var core = require('web.core');
    var KanbanController = require('web.KanbanController');
    var KanbanView = require('web.KanbanView');
    var viewRegistry = require('web.view_registry');

    var AddKanbanViewController = KanbanController.extend({
        buttons_template: 'AddsKanbanView.buttons',

        renderButtons: function () {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                var self = this;
                this.$buttons.on('click', '.o_button_add_kanban_btn', function () {
                    return self._rpc({
                        model: 'edition.store',
                        method: 'update_edition_store_button',
                        args: [self.getSelectedIds()],
                    }).then(function(res){
                        location.reload();  // 更新后刷新页面
                    });
                });
            }
        }
    });

    var AddsKanbanView = KanbanView.extend({
        config: _.extend({}, KanbanView.prototype.config, {
            Controller: AddKanbanViewController,
        }),
    });

    viewRegistry.add('add_buttons_kanban', AddsKanbanView);
});
