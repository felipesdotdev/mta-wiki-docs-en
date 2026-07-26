---
doc_id: "mta-wiki:10828"
title: "DGS Functions and GUI Functions"
source_title: "DGS Functions and GUI Functions"
source_url: "https://wiki.multitheftauto.com/wiki/DGS_Functions_and_GUI_Functions"
revision_id: 71076
language: "en"
categories: []
generated_at: "2026-07-26T16:11:19.244682+00:00"
---

# DGS Functions and GUI Functions

This page shows the functions between **[DGS](mta://reference/misc/dgs.md)** and **GUI**. If you want to convert **GUI** to **[DGS](mta://reference/misc/dgs.md)**, Please read following table.

| GUI Functions | DGS Functions |
| --- | --- |
| guiGetPosition | dgsGetPosition |
| guiSetPosition | dgsSetPosition |
| getElementParent | dgsGetParent |
| setElementParent | dgsSetParent |
| getElementChild | dgsGetChild |
| getElementChildren | dgsGetChildren |
| guiGetSize | dgsGetSize |
| guiSetSize | dgsSetSize |
| getElementType | dgsGetType |
| guiGetProperty | dgsGetProperty |
| guiSetProperty | dgsSetProperty |
| guiGetProperties | dgsGetProperties |
| guiGetVisible | dgsGetVisible |
| guiSetVisible | dgsSetVisible |
| guiGetEnabled | dgsGetEnabled |
| guiSetEnabled | dgsSetEnabled |
| guiGetAlpha | dgsGetAlpha |
| guiSetAlpha | dgsSetAlpha |
| guiGetFont | dgsGetFont |
| guiSetFont | dgsSetFont |
| guiGetText | dgsGetText |
| guiSetText | dgsSetText |
| guiCreateFont | dgsCreateFont |
| guiBringToFront | dgsBringToFront |
| guiCreateBrowser | dgsCreateBrowser |
| guiCreateButton | dgsCreateButton |
| guiCreateCheckBox | dgsCreateCheckBox |
| guiCheckBoxGetSelected | dgsCheckBoxGetSelected |
| guiCheckBoxSetSelected | dgsCheckBoxSetSelected |
| guiCreateComboBox | dgsCreateComboBox |
| guiComboBoxAddItem | dgsComboBoxAddItem |
| guiComboBoxRemoveItem | dgsComboBoxRemoveItem |
| guiComboBoxSetItemText | dgsComboBoxSetItemText |
| guiComboBoxGetItemText | dgsComboBoxGetItemText |
| guiComboBoxClear | dgsComboBoxClear |
| guiComboBoxSetSelected | dgsComboBoxSetSelectedItem |
| guiComboBoxGetSelected | dgsComboBoxGetSelectedItem |
| guiCreateEdit | dgsCreateEdit |
| guiEditGetMaxLength | dgsEditGetMaxLength |
| guiEditSetMaxLength | dgsEditSetMaxLength |
| guiEditSetReadOnly | dgsEditSetReadOnly |
| guiEditIsReadOnly | dgsEditGetReadOnly |
| guiEditSetMasked | dgsEditSetMasked |
| guiEditIsMasked | dgsEditGetMasked |
| guiCreateGridList | dgsCreateGridList |
| guiGridListAddColumn | dgsGridListAddColumn |
| guiGridListGetColumnCount | dgsGridListGetColumnCount |
| guiGridListRemoveColumn | dgsGridListRemoveColumn |
| guiGridListGetColumnWidth | dgsGridListGetColumnWidth |
| guiGridListSetColumnWidth | dgsGridListSetColumnWidth |
| guiGridListGetColumnTitle | dgsGridListGetColumnTitle |
| guiGridListSetColumnTitle | dgsGridListSetColumnTitle |
| guiGridListAddRow | dgsGridListAddRow |
| guiGridListRemoveRow | dgsGridListRemoveRow |
| guiGridListClear | dgsGridListClear |
| guiGridListGetRowCount | dgsGridListGetRowCount |
| guiGridListSetItemText | dgsGridListSetItemText dgsGridListSetRowAsSection |
| guiGridListGetItemText | dgsGridListGetItemText |
| guiGridListGetSelectedItem | dgsGridListGetSelectedItem |
| guiGridListSetSelectedItem | dgsGridListSetSelectedItem |
| guiGridListSetItemColor | dgsGridListSetItemColor |
| guiGridListGetItemColor | dgsGridListGetItemColor |
| guiGridListSetItemData | dgsGridListSetItemData |
| guiGridListGetItemData | dgsGridListGetItemData |
| guiGridListSetSelectionMode | dgsGridListSetSelectionMode |
| guiGridListGetSelectedItems | dgsGridListGetSelectedItems |
| guiCreateStaticImage | dgsCreateImage |
| guiStaticImageLoadImage | dgsImageSetImage |
| guiCreateMemo | dgsCreateMemo |
| guiMemoSetVerticalScrollPosition | dgsMemoSetScrollPosition |
| guiMemoGetVerticalScrollPosition | dgsMemoGetScrollPosition |
| guiMemoSetReadOnly | dgsMemoSetReadOnly |
| guiCreateLabel | dgsCreateLabel |
| guiLabelSetColor | dgsLabelSetColor |
| guiLabelGetColor | dgsLabelGetColor |
| guiLabelSetHorizontalAlign | dgsLabelSetHorizontalAlign |
| guiLabelSetVerticalAlign | dgsLabelSetVerticalAlign |
| guiCreateProgressBar | dgsCreateProgressBar |
| guiProgressBarGetProgress | dgsProgressBarGetProgress |
| guiProgressBarSetProgress | dgsProgressBarSetProgress |
| guiCreateRadioButton | dgsCreateRadioButton |
| guiRadioButtonGetSelected | dgsRadioButtonGetSelected |
| guiRadioButtonSetSelected | dgsRadioButtonSetSelected |
| guiCreateScrollBar | dgsCreateScrollBar |
| guiScrollBarSetScrollPosition | dgsScrollBarSetScrollPosition |
| guiScrollBarGetScrollPosition | dgsScrollBarGetScrollPosition |
| guiCreateScrollPane | dgsCreateScrollPane |
| guiCreateTabPanel | dgsCreateTabPanel |
| guiCreateTab | dgsCreateTab |
| guiGetSelectedTab | dgsGetSelectedTab |
| guiSetSelectedTab | dgsSetSelectedTab |
| guiDeleteTab | dgsDeleteTab |
| guiCreateWindow | dgsCreateWindow |
| guiWindowSetSizable | dgsWindowSetSizable |
| guiWindowSetMovable | dgsWindowSetMovable |
| guiSetInputEnabled | dgsSetInputEnabled |

## See Also

[DGS Events and GUI Events](mta://scripting/concepts/dgs-events-and-gui-events.md)
