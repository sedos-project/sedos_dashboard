
htmx.on("htmx:afterSwap", function(evt) {
    renderTables();
});

$('document').ready(renderTables);


function renderTables() {
    tables = document.querySelectorAll("table");
    for (const table of tables) {
        makeDataTable($(table));
    }
}


function makeDataTable(table) {
    table.DataTable(
        {
            scrollX: true,
            columnDefs: [
                {
                    target: "_all",
                    render: prepareJson,
                    createdCell: renderJson
                }
            ]
        });
}


function prepareJson(data, type, row, meta) {
    if (data.startsWith("{")) {
        return "<pre></pre>";
    }
    return data;
}

function renderJson(td, data, row) {
    if (data.startsWith("{")) {
        const json_data = JSON.parse(data.replaceAll("'", '"'));
        $(td).find('pre').jsonViewer(json_data, {collapsed: true});
    }
}
