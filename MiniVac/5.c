#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>  // ���丮 ���� ������� 
#include <string.h>
#include <sys/stat.h> // ������ ���� ���� ������� 
#include <unistd.h> // �������� �ڷ���
#include "md5.h"

#define BUF_SIZE 2048
#define db_Num 3

//  ���, �̸�, ���ϰ���, �˻�� ���� ���� 
char way[BUF_SIZE];
char name[BUF_SIZE];
int file_num, virus_num;

// db �̸� / ���̷��� ���� 
struct dbInfo{
	char name[30];
	char *str;
};

struct dbInfo db[db_Num]={
	{"EICAR", "44d88612fea8a8f36de82e1278abb02f"},
	{"Test", "77bff0b143e4840ae73d4582a8914a43"},
	{"EICAR2", "6a4cd5563a37ee5b97a319a27066d8c6"},
};

// MD5 �ؽð� ��ȯ 
char *md5(char *msg){
	int i = 0;
	unsigned char digest[16] = {0,};
	static char out_Hash[50] = {0,};
	md5_st md5_ctx;
	
	md5_init(&md5_ctx);
	md5_convert(&md5_ctx, msg, strlen(msg));
	md5_gethash(&md5_ctx, digest);
	
	for (i = 0; i<16; i++)
        sprintf(out_Hash + (i * 2), "%02x", digest[i]);
	
	return out_Hash;
}

// �˻���� 
int scan(const char* path){
	DIR *dr = NULL;
	struct dirent *de = NULL;
	struct stat fi;
	char fn[BUF_SIZE];
	char *buf_MD5;
	FILE *fp;
	int i;
	
	if((dr = opendir(path)) == NULL){
		printf("%s\n", path);
		printf("Could not open directory");
	}
	
	while((de = readdir(dr)) != NULL){
		char buf[BUF_SIZE]={0,};
		if(strcmp(de->d_name, ".") == 0 || strcmp(de->d_name, "..") == 0)
			continue;
		
		sprintf(fn, "%s/%s", path, de->d_name);
		
		
		if(stat(fn, &fi) == -1){
			continue;
		}
		
		if(S_ISDIR(fi.st_mode)){
			scan(fn);
		}else if(S_ISREG(fi.st_mode)){
			fp = fopen(fn, "rb");
			
			if(fp==NULL){
				perror("File open failed\n");
				exit(0);
			}
			
			fread(buf, sizeof(buf), 1, fp);
			fclose(fp);
			buf_MD5 = md5(buf);
			
			for(i = 0; i<db_Num; i++){
				if(!strcmp(buf_MD5, db[i].str)){
					chmod(fn, 0777);
					strcat(way, fn);
					strcat(way, ",");
					strcat(name, db[i].name);
					strcat(name, ",");
					virus_num++;
				}
			}
		}
		file_num++;
	}
	closedir(dr);
	return 1;
}

char *r_way(){
	return way;
}

char *r_name(){
	return name;
}

int r_filenum(){
	return file_num;
}

int r_virusnum(){
	return virus_num;
}

// �ʱ�ȭ 
void init(){
	strcpy(way, "\0");
	strcpy(name, "\0");
	file_num = 0;
	virus_num = 0;
}
