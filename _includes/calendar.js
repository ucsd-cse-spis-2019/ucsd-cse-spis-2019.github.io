

function setUpCalendar(page) {
    addCalendarTable(page,cal);
    reportDaysOutsideCalendar(page,cal);    
}

function weekLabel(weekNum) {
 // returns HTML content of <td> element at start of week
    return 'Week ' + weekNum +  
	'<ul>' +
	'<li><a href="{{site.weekly_google_calendar_prefix}}' +
	weekNum + '">agenda</a></li>' +
	'<li><a href="/lectures/week' + weekNum + '">lectures</a></li>' +
	'</ul>';
}

function linkToLecture(mm,dd,week) {
    return '<a href="/lectures/week' + week + '/' + mm + dd +'/">' +
	mm + '/' + dd +
	'</a>';
}

function dayLabel(thisDay, week) {
    // thisDay is a momentjs instance
    mm = thisDay.format("MM");
    dd = thisDay.format("DD");    
    ddd = thisDay.format("ddd");
    if  ( ["Mon","Tue","Wed","Thu","Fri"].indexOf(ddd) == -1 &&
	  ! ( thisDay.isSame(moment(cal.startDate))) )
	return mm + "/" + dd; // plain old date
    else
	return linkToLecture(mm,dd,week);

}


function addCalendarTable(page,cal) {
    
    $(page).find('#calendar').empty();
    $(page).find('#calendar').append(  '<table >' );
    $(page).find('#calendar table').append( '<tr><th>&nbsp;</th><th>S</th><th>M</th><th>T</th><th>W</th><th>R</th><th>F</th><th>S</th></tr>');
    var thisDay = new moment(cal.startDate);
    for(var week=1;week<=cal.numWeeks; week++){
	$(page).find('#calendar table').append( '<tr data-week-num="' + week +'" />')
	var thisWeeksTrSelector = '#calendar table tr[data-week-num="' + week + '"]';
	$(page).find(thisWeeksTrSelector).append('<td class="week">' + weekLabel(week) + '</td>');
	for (var day=1; day<=7; day++) {
	    var thisDateFormatted = thisDay.format("MM/DD");
	    var cal_mmdd = $('<div class="cal_mmdd">' +
			     dayLabel(thisDay,week) +
			     '</div>');
	    var assignments = getAssignments(cal,thisDateFormatted);
	    var td = $('<td/>')
		.append(cal_mmdd)
		.append(assignments)
		.attr('data-mmdd',thisDateFormatted)
	    $(page).find(thisWeeksTrSelector).append(td);
	    thisDay = thisDay.add(1,'days');
	}
    }


}


function reportDaysOutsideCalendar(page,cal) {
    if (cal.days_outside_calendar.length > 0) {
	$(page).find('#calendar').append(  '<div class="calendar-errors" />' );
	$(page).find('#calendar div.calendar-errors').append("<h2>Warning: there were some calendar errors:</h2>");
	for (var i=0, len=cal.days_outside_calendar.length; i<len; i++) {
	    $(page).find('#calendar div.calendar-errors').append("<p><code>" +
						      JSON.stringify(cal.days_outside_calendar[i]) +
						      "</p>");
	}
    }
}

$(document).on('pageinit','[data-role=page]', function(){
    console.log("calendar.js: pageinit");
    setUpCalendar($(this));
    populateAssignmentElements($(this));    
    console.log("calendar.js: pageinit done");
});

