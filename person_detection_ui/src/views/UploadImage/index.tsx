import { Button, Upload, UploadFile, UploadProps } from 'antd';
import { UploadOutlined } from '@ant-design/icons';
import { useState } from 'react';
import { useUploadImageMutation } from '../../store/image/api';

export default function UploadImage(): JSX.Element {
  const [fileList, setFileList] = useState<UploadFile[]>([]);

  const [uploadImage] = useUploadImageMutation();

  const handleChange = (info: UploadProps) => {
    if (info.fileList) {
      setFileList(info.fileList);
      console.log(info.fileList);
    }
  };

  const handleUploadImage = () => {
    const formData = new FormData();

    fileList.forEach((f) => {
      if (f.originFileObj) {
        formData.append('image', f.originFileObj);
      }
    });

    uploadImage(formData);
  };

  const boxStyle = 'flex flex-col w-full gap-1 border border-stone-300 rounded-lg p-5';

  return (
    <div className="flex w-full gap-5">
      <div className={boxStyle}>
        <p>Tutaj wgraj pliki:</p>
        <Upload
          maxCount={1}
          fileList={fileList}
          accept="image/png, image/jpeg"
          beforeUpload={() => false}
          onChange={handleChange}>
          <Button icon={<UploadOutlined />}>Upload</Button>
        </Upload>
      </div>
      <div className={boxStyle}>
        <span>Wyślij dodane zdjęcia aby zlokalizować ilość osób na zdjęciu</span>
        <Button disabled={!fileList.length} onClick={handleUploadImage}>
          Wyślij
        </Button>
      </div>
      {/* <input type="file" onChange={(event) => console.log(event.target.value)} /> */}
    </div>
  );
}
