function exportFormItemsWithChoices() {
  var form = FormApp.openById('1RHBxJhnHdJj7N8j-7P3phA-4JA90H8zhJWUnQ-s1yqs'); // ID Form của bạn
  var items = form.getItems();
  var data = [];

  for (var i = 0; i < items.length; i++) {
    var item = items[i];
    var itemType = item.getType();
    var choices = null;

    try {
      if (itemType === FormApp.ItemType.MULTIPLE_CHOICE) {
        choices = item.asMultipleChoiceItem().getChoices().map(function(choice) {
          return choice.getValue();
        });
      } else if (itemType === FormApp.ItemType.CHECKBOX) {
        choices = item.asCheckboxItem().getChoices().map(function(choice) {
          return choice.getValue();
        });
      } else if (itemType === FormApp.ItemType.LIST) {
        choices = item.asListItem().getChoices().map(function(choice) {
          return choice.getValue();
        });
      } else if (itemType === FormApp.ItemType.GRID || itemType === FormApp.ItemType.CHECKBOX_GRID) {
        var gridItem = item.asGridItem();
        choices = {
          rows: gridItem.getRows(),
          columns: gridItem.getColumns()
        };
      }
    } catch (error) {
      Logger.log("Lỗi xử lý mục: " + item.getTitle() + " - " + error.message);
    }

    data.push({
      title: item.getTitle(),
      id: item.getId(),
      type: itemType,
      choices: choices
    });
  }

  Logger.log(JSON.stringify(data, null, 2)); // Xuất ra log để kiểm tra
}
