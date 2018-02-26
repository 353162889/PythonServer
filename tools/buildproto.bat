for /f "delims=\" %%a in ('dir /b /a-d /o-d "./protofiles/"') do protoc -I=./protofiles/ --python_out=../server/protobuf ./protofiles/%%a
pause