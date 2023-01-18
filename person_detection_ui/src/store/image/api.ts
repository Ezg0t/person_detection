import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const imageApi = createApi({
  reducerPath: 'imageApi',
  baseQuery: fetchBaseQuery({
    baseUrl: '/api',
  }),
  endpoints: (build) => ({
    uploadImage: build.mutation({
      query: (formData) => ({
        url: '/images',
        method: 'POST',
        body: formData,
      }),
    }),
  }),
});

export const { useUploadImageMutation } = imageApi;

export default imageApi;
