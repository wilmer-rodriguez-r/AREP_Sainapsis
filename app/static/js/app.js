app = (function (api) {
    let _publicFunctions = {};


    let _update = function (data) {
        $(document).ready(() => {
            $("#getrespmsg").html(data);
        });
    }

    let get = function (query) {
        api.get(query, _update);
    }

    _publicFunctions.onSumbit = function (event) {
        let query = $("#query").val();
        get(query)
    }

    return _publicFunctions;
})(apiclient);