function shaping_json($this) {
    if ($this.value != '') {
        try {
            var json = $.parseJSON($this.value);
            $('#json_check').removeClass('has-error');
            $('#send_json').attr('name', 'json');
        } catch (e) {
            $('#json_check').addClass('has-error');
            $('#send_json').removeAttr('name');
            //alert('正しいJSON形式で入力してください');
        }
    } else {
        $('#json_check').removeClass('has-error');
        $('#send_json').removeAttr('name');
    }
}

function verification() {
    var input_json = $.trim($('#input_json').val());
    if (!input_json.length) {
        return true;
    } else {
        try {
            var json = $.parseJSON(input_json);
            $('#json_check').removeClass('has-error');
            $('#send_json').attr('name', 'json');
            var new_json = input_json.replace(/ /g, '');
            new_json = new_json.replace(/\n/g, '');
            new_json = new_json.replace(/\t/g, '');
            $('#send_json').attr('value', new_json);
            return true;
        } catch (e) {
            $('#json_check').addClass('has-error');
            $('#send_json').removeAttr('name');
            alert('正しいJSON形式で入力してください\n' + e);
            return false;
        }
    }
}

$("#show_password").change(function() {
    if ($('#input_password').attr('type') == 'password') {
        $('#input_password').attr('type', 'text');
    } else {
        $('#input_password').attr('type', 'password');
    }
});

$(function () {
    $("#datetimepicker").datetimepicker({
        language: "ja",
        format: "YYYY/MM/DD hh:mm a",
        minDate: moment(),
    });
});

$('tr[data-href]').addClass('clickable')
    .click(function(e) {
    if($(e.target).is('td,th')) {
        window.location = $(e.target).closest('tr').data('href');
    };
});

$('#destory_develop').click(function() {
    if (confirm('本当に削除しますか？')) {
        var url = $(this).attr('data-url');
        $.ajax({
            url: url,
            type: "POST",
            data: {'pem_type': 'develop'},
            success: function (result) {
                location.href = url + "?result=develop_success";
            }
        });
    }
});

$('#destory_product').click(function() {
    if (confirm('本当に削除しますか？')) {
        var url = $(this).attr('data-url');
        $.ajax({
            url: url,
            type: "POST",
            data: {'pem_type': 'product'},
            success: function (result) {
                location.href = url + "?result=product_success";
            }
        });
    }
})
