# Creating a scene

 본 섹션의 목표는 three.js를 간략하게 소개하는 것이다. 우리는 회전하는 정육면체로 scene을 설치하는 것으로 시작할 것이다. 작업 예제는 페이지 하단에 제공되며, 당신이 막혀서 도움이 필요할 때를 대비한 것이다.

## 시작 전에

 시작 전에 three.js을 가져올 필요가 있다. 컴퓨터의 파일에, three.js의 파일 경로를 다음과 같이  브라우저에서 열어 HTML에 저장한다. 

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>My first three.js app</title>
		<style>
			body { margin: 0; }
			canvas { width: 100%; height: 100% }
		</style>
	</head>
	<body>
		<script src="js/three.js"></script>
        // 파일 경로를 저장한다.
		<script>
			// Our Javascript will go here.
		</script>
	</body>
</html>
```

 ## scene 만들기

실제로 three.js으로 보여주기 위해서  3가지(장면, 카메라 및 렌더러)가 필요하다. 

```