#include <stdio.h>
#include <malloc.h>
#include <string.h>

#define leftrotation(x, c) (((x) << (c)) | ((x) >> (32 - (c))))
#define md5_bytes 64
#define md5_buf_size (md5_bytes*2)

// 블럭 4개, 문자열 버퍼 
typedef struct _md5_st{
	unsigned int b0;
	unsigned int b1;
	unsigned int b2;
	unsigned int b3;

	char buf[md5_buf_size];
	unsigned int buf_stored_len;

	unsigned __int64 updated_len;
}md5_st;

// 라운드당 시프트 
static const unsigned int md5_r[md5_bytes] = {
	7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
	5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
	4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
	6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
};

// K 값 테이블 
static const unsigned int md5_k[md5_bytes] = {
	0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
	0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,

	0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
	0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,

	0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
	0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,

	0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
	0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
};

// 완성된 해쉬코드 넣는 함수 
void md5_puthash(unsigned int hash, unsigned char *dst){
	if (!dst) return;

	dst[0] = (unsigned char)(hash);
	dst[1] = (unsigned char)(hash >> 8);
	dst[2] = (unsigned char)(hash >> 16);
	dst[3] = (unsigned char)(hash >> 24);
}

// 메인 루프 
int md5_block_update(md5_st *ctx, char *block){
	int i = 0;
	unsigned int a,b,c,d;
	unsigned int *w;

	if (!ctx || !block)
	return -1;

	a = ctx->b0;
	b = ctx->b1;
	c = ctx->b2;
	d = ctx->b3;
	w = (unsigned int*)block;

	// 메인 라운드 
	while (i < md5_bytes){
		unsigned int f = 0;
		unsigned int g = 0;
		unsigned int temp = 0;

		if (i < 16){
			f = (b & c) | ((~b) & d);
			g = i;
		}else if (i < 32){
			f = (d & b) | ((~d) & c);
			g = (5 * i + 1) % 16;
		}else if (i < 48){
			f = b ^ c ^ d;
			g = (3 * i + 5) % 16;
		}else{
			f = c ^ (b | (~d));
			g = (7 * i) % 16;
		}

		temp = d;
		d = c;
		c = b;
		b = b + leftrotation((a + f + md5_k[i] + w[g]), md5_r[i]);
		a = temp;

		i++;
	}

	// 해쉬 결과 추가 
	ctx->b0 += a;
	ctx->b1 += b;
	ctx->b2 += c;
	ctx->b3 += d;
	ctx->updated_len += md5_bytes;
 
	return 0;
}

// 초기화 
int md5_init(md5_st *ctx){
	if(!ctx) return -1;

	memset(ctx, 0, sizeof(md5_st));

	ctx->b0 = 0x67452301;
	ctx->b1 = 0xefcdab89;
	ctx->b2 = 0x98badcfe;
	ctx->b3 = 0x10325476;

	ctx->buf_stored_len = 0;
	ctx->updated_len = 0;

	return 0;
}

// 메시지를 512bit로 자르는 함수 
int md5_convert(md5_st *ctx, char *msg, int msg_len){
	int remain_len = msg_len;
	int offset = 0;

	if (!ctx || !msg || msg_len <= 0) return -1;
	if (ctx->buf_stored_len < 0) return -1;

	if (ctx->buf_stored_len > 0){
		int to_copy_len = md5_bytes - ctx->buf_stored_len;
		to_copy_len = (to_copy_len > remain_len) ? remain_len : to_copy_len;

		memcpy(&ctx->buf[ctx->buf_stored_len], msg, to_copy_len);

		ctx->buf_stored_len += to_copy_len;
		remain_len -= to_copy_len;
		offset += to_copy_len;

		if (ctx->buf_stored_len == md5_bytes){
			md5_block_update(ctx, ctx->buf);
			ctx->buf_stored_len = 0;
		}
	}

	while (remain_len >= md5_bytes){
		md5_block_update(ctx, &msg[offset]);

		remain_len -= md5_bytes;
		offset += md5_bytes;
	}

	if (remain_len){
		memcpy(ctx->buf, &msg[offset], remain_len);
		ctx->buf_stored_len = remain_len;
	}
 
	return 0;
}

// 나머지 데이터 처리 후 반환 
int md5_gethash(md5_st *ctx, unsigned char digest[16]){
	int offset = 0;
	unsigned __int64 total_msg_bits_size = 0;

	if (!ctx) return -1;

	offset = ctx->buf_stored_len;
	total_msg_bits_size = 8 * (ctx->updated_len + (unsigned __int64)ctx->buf_stored_len);

	ctx->buf[offset++] = 128;
	memset(&ctx->buf[offset], 0, md5_buf_size - offset);

	if (offset <= md5_bytes - sizeof(__int64)){
		offset = md5_bytes - sizeof(__int64);
	}else{
		offset = md5_buf_size - sizeof(__int64);
	}

	// 리틀 엔디안 
	memcpy(&ctx->buf[offset], &total_msg_bits_size, sizeof(__int64));
	offset += sizeof(__int64);

	md5_block_update(ctx, ctx->buf);
	if (offset > md5_bytes) md5_block_update(ctx, &ctx->buf[md5_bytes]);
	
	// 해쉬코드 넣어서 반환 
	md5_puthash(ctx->b0, digest);
	md5_puthash(ctx->b1, digest + 4);
	md5_puthash(ctx->b2, digest + 8);
	md5_puthash(ctx->b3, digest + 12);

	return 0;
}
