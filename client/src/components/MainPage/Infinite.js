import React, { useState, useEffect } from "react";
import InfiniteScroll from "react-infinite-scroll-component";
import { Loader } from "./Loader";
import ItemInfo from "./ItemInfo";

export default function Infinite({ child }) {
  const [images, setImages] = useState([]);
  const [count, setCount] = useState(1);

  const fetchImages = (cnt) => {
    setImages([...images, cnt, cnt + 1, cnt + 2, cnt + 3]);
    setCount(cnt + 4);
  };

  useEffect(() => {
    fetchImages(count);
  }, []);

  return (
    <InfiniteScroll
      style={{ display: "flex", flexWrap: "wrap" }}
      dataLength={images.length}
      next={() => fetchImages(count)}
      hasMore={count < 100 ? true : false}
      loader={<Loader />}
      endMessage={<p>You have seen it all</p>}
    >
      {images.map((idx) => (
        <ItemInfo key={idx} idx={idx} />
      ))}
    </InfiniteScroll>
  );
}
