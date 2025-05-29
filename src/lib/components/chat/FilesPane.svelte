<script lang="ts">
	import { toast } from 'svelte-sonner';
	import FileItem from '../common/FileItem.svelte';
	import Image from '../common/Image.svelte';
	import { deleteFileById } from '$lib/apis/files';
	import { getContext } from 'svelte';

	const i18n = getContext('i18n');

	interface FileType {
		id?: string;
		type: string;
		url: string;
		name?: string;
		size?: number;
		status?: string;
		collection?: boolean;
	}

	export let files: FileType[] = [];
</script>

<div class="h-full w-full p-4 bg-gray-50 dark:bg-gray-950 overflow-y-auto">
	<h2 class="text-lg font-semibold mb-4 dark:text-gray-100">Files</h2>

	{#if files.length > 0}
		<div class="flex flex-col gap-3">
			{#each files as file, fileIdx}
				{#if file.type === 'image'}
					<div class="relative group">
						<div class="relative">
							<Image src={file.url} alt="input" imageClassName="w-full rounded-xl object-cover" />
						</div>
						<div class="absolute -top-1 -right-1">
							<button
								class="bg-white text-black border border-white rounded-full group-hover:visible invisible transition"
								type="button"
								on:click={() => {
									files.splice(fileIdx, 1);
									files = files;
								}}
							>
								<svg
									xmlns="http://www.w3.org/2000/svg"
									viewBox="0 0 20 20"
									fill="currentColor"
									class="w-4 h-4"
								>
									<path
										d="M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z"
									/>
								</svg>
							</button>
						</div>
					</div>
				{:else}
					<FileItem
						item={file}
						name={file.name}
						type={file.type}
						size={file?.size}
						loading={file.status === 'uploading'}
						dismissible={true}
						edit={true}
						on:dismiss={async () => {
							try {
								if (file.type !== 'collection' && !file?.collection) {
									if (file.id) {
										await deleteFileById(localStorage.token, file.id);
									}
								}
							} catch (error) {
								console.error('Error deleting file:', error);
							}
							files.splice(fileIdx, 1);
							files = files;
						}}
						on:click={() => {
							console.log(file);
						}}
					/>
				{/if}
			{/each}
		</div>
	{:else}
		<div class="text-gray-500 dark:text-gray-400 text-center">No files uploaded yet</div>
	{/if}
</div>
