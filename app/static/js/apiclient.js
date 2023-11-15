apiclient = (function () {

    let _publicFunctions = {};

    _publicFunctions.get = function (query, callback) {
        return $.get(`/openai/${query}`, (data) => {
            callback(data);
        }).fail();
    }

    return _publicFunctions;
})()