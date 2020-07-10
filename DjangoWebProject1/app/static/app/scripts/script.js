function formatNumber(n) {
    // format number 1000000 to 1,234,567
    return n.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}


$('#assetcost, #assetvalue').keyup(function () {
    var value1 = parseFloat($('#assetcost').val()) || 0;
    var value2 = parseFloat($('#assetvalue').val()) || 0;
    
    $('#totassetcost').val(value1 + value2);
});