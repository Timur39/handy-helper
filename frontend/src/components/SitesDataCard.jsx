import React from 'react';
import { Card, Col, Row } from 'antd';


let clickLink = ''

const SitesDataCard = ({ title, icon, data, fields, isLoading }) => {
  const dataArray = Object.values(data || {});
  

  return (
    <div>
      <Col span={24}>
        <Card className='w-[100%] mx-auto' 
          loading={isLoading}
          size='small'
          type='inner'
          title={
            <div className="flex items-center gap-4">
              {icon && <img src={icon} alt="icon" />}
              <h1>{title}</h1>
            </div>
          }
        >
          {dataArray.length > 0 ? (
          dataArray.map((item, index) => (
            <div key={index}  className='flex flex-auto mb-4' >
              <Card size="small" 
                className='w-[100%] h-auto' 
                hoverable={true} 
                onClick={() => {
                  const link = fields.find((field) => field.isLink)?.key;
                  if (link && item[link]) {
                    window.open(item[link], '_blank', 'noopener,noreferrer');
                  }
                }} > 
              {fields.map((field) => (
                field.label !== "Ссылка" & field.label !== "Ссылка на автора" ? (

                <p key={field.key}>
                  <strong>{field.label}:</strong>{" "}

                  {field.isList ? (
                    item[field.key]?.join(", ") || "Нет данных"
                  ) : field.isImg ? (
                    <img src={item[field.key]}></img>
                  ) : field.IsDate ? (
                    item[field.key] || "Нет данных"
                  ) : !field.isLink ? (
                    item[field.key] || "Нет данных"
                  ) : null
                  }
                    </p>
                  ) : null
                  ))}
                
                </Card>
              </div>
            ))
          ) : (
            <p>Загрузка...</p>
          )}
        </Card>
      </Col>
    </div>
  );
};

export default SitesDataCard
  