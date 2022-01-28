// 엘리먼트들에 대한 데이터를 테이블 형식으로 화면에 표현

function makeTable(elem){
	var $table = $("<table border=1>");	// 테이블 테두리 속성값 1 (HTML 형태)
	
	// column 정의
	for(var i = 0 ; i < 1 ; i++){
		var $tr=$("<tr>");	// 표 맨 위에 있는 카테고리 (반복문 1회만 실행)

		for(var j = 0 ; j < elem.eq(0).children().length ; j++) {
			var $td = $("<td>").append(elem.eq(0).children().eq(j).prop("tagName"));
			// 데이터의 0번째 요소의 자식요소를 탐색하고, 그 중에서 j번째 요소를 가져와서 변수 $td에 저장
			$tr.append($td);
			// $tr에 하나씩 추가 (총 5번)
		}
		$table.append($tr);
		// 다 $tr로 추가되면 table에 추가
	}
	
	// data 넣기
	for(var i = 0 ; i < elem.length ; i++){ // 데이터 갯수만큼 반복 : 107번
		var $tr=$("<tr>");	// $tr에 <tr> 속성을 적용

		for(var j = 0 ; j < elem.eq(i).children().length ; j++){  // 데이터 각각의 요소 길이만큼 반복 : 5번
			var $td = $("<td>").append(elem.eq(i).children().eq(j).text());
			// td에 각각의 컬럼에 해당하는 내용 저장 (5번)

			$tr.append($td);
			// $td에 한줄씩 저장한 내용을 $tr에 한번에 추가
		}
		$table.append($tr);
	}
	
	// 만들어진 table 반환
	return $table;
}



