
        $(document).ready(function() {
            $("th.sortable").click(function() {
                var table = $(this).parents("table").eq(0);
                var rows = table.find("tr:gt(0)").toArray().sort(compare($(this).index()));
                this.asc = !this.asc;
                if (!this.asc){
                    rows = rows.reverse();
                }
                for (var i = 0; i < rows.length; i++){
                    table.append(rows[i]);
                }
                $("th.sortable").removeClass("asc desc");
                if (this.asc) {
                    $(this).addClass("asc");
                } else {
                    $(this).addClass("desc");
                }
            });
        });

        function compare(index) {
            return function(a, b) {
                var valA = getCellValue(a, index);
                var valB = getCellValue(b, index);
                return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.toString().localeCompare(valB);
            }
        }

        function getCellValue(row, index) {
            return $(row).children("td").eq(index).text();
        }
   