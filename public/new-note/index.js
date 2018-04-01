//text edit

$('#note-title').click(function() {
	const range = rangy.createRange()
	range.selectNodeContents($(this)[0])
	rangy.getSelection().setSingleRange(range)
	$(this).removeClass('placeholder')
})

$('#note-title').keydown(function(e) {
	if(e.keyCode == 13) {	
		$(this).blur()
	}
})
//highlight

rangy.init()
const highlighter = rangy.createHighlighter()
highlighter.addClassApplier(rangy.createClassApplier('highlight', {
	ignoreWhiteSpace: true,
	elementTagName: 'span',	
	tagNames: ['span'],
	elementProperties: {
		onclick: function() {
			var highlight = highlighter.getHighlightForElement(this)
			highlighter.removeHighlights( [highlight] )
		}
	}
}));

const highlightSelection = () => {
	highlighter.highlightSelection('highlight', { containerElementId: 'transcript' })
	rangy.getSelection().removeAllRanges()
}

$('body').mouseup(highlightSelection)
$('body').mouseleave(highlightSelection)

const recognition = new webkitSpeechRecognition()
recognition.continuous = true
recognition.interimResults = true

var isFirst = true

//recog

const restartRecognition = () => {
	$('#transcript').children().last().removeClass('interim')
	recognition.start()
}

recognition.onstart = () => {
	isFirst = true
}

recognition.onresult = (event) => {
	$('#transcript').scrollTop($('#transcript').height())
	console.log(event.results[0])
	const text = $('<span></span>')
	text.text(event.results[0][0].transcript)
	text.append($('<br/>'))
	text.addClass('interim')
	if (isFirst) {
		$('#transcript').append(text)
		isFirst = false
	} else {
		$('#transcript').children().last().replaceWith(text)
	}
	if (event.results[0].isFinal) {
		recognition.stop()
	}
}

recognition.onerror = () => {
	recognition.stop()
}

recognition.onnomatch = () => {
	recognition.stop()
}

recognition.onend = restartRecognition
recognition.onpause = restartRecognition

$(document).ready(() => {
	recognition.start()
})
