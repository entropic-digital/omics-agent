<script lang="ts">
	import { onMount } from 'svelte';
	import { WEBUI_BASE_URL } from '$lib/constants';

	interface FileNode {
		type: 'file';
		size: number;
		last_modified: string;
	}

	interface DirectoryNode {
		type: 'directory';
		contents: Record<string, FileNode | DirectoryNode>;
	}

	type TreeNode = FileNode | DirectoryNode;

	interface TreeItem {
		name: string;
		type: 'file' | 'folder';
		level: number;
		children?: TreeItem[];
		size?: string;
		lastModified?: string;
	}

	let fileTree: Record<string, TreeNode> = {};
	let loading = true;
	let error: string | null = null;

	// Convert bytes to human readable format
	function formatBytes(bytes: number): string {
		if (bytes === 0) return '0 Bytes';
		const k = 1024;
		const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
		const i = Math.floor(Math.log(bytes) / Math.log(k));
		return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
	}

	// Format date to local string
	function formatDate(dateStr: string): string {
		return new Date(dateStr).toLocaleDateString();
	}

	// Recursive component to render directory contents
	function renderDirectory(contents: Record<string, TreeNode>, level: number = 0): TreeItem[] {
		return Object.entries(contents).map(([name, node]): TreeItem => {
			if (node.type === 'directory') {
				return {
					name,
					type: 'folder',
					level,
					children: renderDirectory(node.contents, level + 1)
				};
			} else {
				return {
					name,
					type: 'file',
					level,
					size: formatBytes(node.size),
					lastModified: formatDate(node.last_modified)
				};
			}
		});
	}

	async function fetchFileTree() {
		try {
			loading = true;
			error = null;

			// this below line was the original way of doing it but it didnt work
			// without a proxy so we added the below line
			// const response = await fetch('/api/files/storage/list');
			const response = await fetch(`${WEBUI_BASE_URL}/api/v1/files/storage/list`);
			if (!response.ok) {
				throw new Error('Failed to fetch file tree');
			}
			fileTree = await response.json();
		} catch (e: unknown) {
			error = e instanceof Error ? e.message : 'An unknown error occurred';
			console.error('Error fetching file tree:', e);
		} finally {
			loading = false;
		}
	}

	$: items = renderDirectory(fileTree);

	onMount(() => {
		fetchFileTree();
	});
</script>

<div class="w-full h-full flex flex-col bg-white dark:bg-gray-850">
	<div class="flex justify-between items-center p-4 border-b border-gray-100 dark:border-gray-800">
		<h2 class="text-lg font-medium text-gray-900 dark:text-gray-100">Data Files</h2>
		<button
			on:click={() => fetchFileTree()}
			class="text-sm px-3 py-1 rounded-md bg-blue-500 text-white hover:bg-blue-600 transition-colors"
		>
			Refresh
		</button>
	</div>

	<div class="flex-1 overflow-y-auto p-2">
		{#if loading}
			<div class="flex justify-center items-center h-full">
				<div class="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-500"></div>
			</div>
		{:else if error}
			<div class="text-red-500 p-4 text-center">
				{error}
			</div>
		{:else if items.length === 0}
			<div class="text-gray-500 dark:text-gray-400 p-4 text-center">No files found</div>
		{:else}
			{#each items as item}
				{#if item.type === 'folder'}
					<div class="hover:bg-gray-50 dark:hover:bg-gray-800 rounded-md">
						<div
							class="flex items-center p-2 cursor-pointer"
							style="padding-left: {item.level * 1}rem"
						>
							<span class="mr-2 opacity-70">📁</span>
							<span class="flex-1 truncate font-medium">{item.name}</span>
						</div>
						{#if item.children}
							{#each item.children as child}
								<div
									class="flex items-center p-2 hover:bg-gray-50 dark:hover:bg-gray-800 cursor-pointer"
									style="padding-left: {child.level * 1.5}rem"
								>
									<span class="mr-2 opacity-70">{child.type === 'folder' ? '📁' : '📄'}</span>
									<span class="flex-1 truncate">{child.name}</span>
									{#if child.type === 'file'}
										<span class="flex gap-4 text-sm text-gray-500 dark:text-gray-400">
											<span>{child.size}</span>
											<span>{child.lastModified}</span>
										</span>
									{/if}
								</div>
							{/each}
						{/if}
					</div>
				{:else}
					<div
						class="flex items-center p-2 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-md cursor-pointer"
						style="padding-left: {item.level * 1}rem"
					>
						<span class="mr-2 opacity-70">📄</span>
						<span class="flex-1 truncate">{item.name}</span>
						<span class="flex gap-4 text-sm text-gray-500 dark:text-gray-400">
							<span>{item.size}</span>
							<span>{item.lastModified}</span>
						</span>
					</div>
				{/if}
			{/each}
		{/if}
	</div>
</div>

<style>
	.file-container {
		background-color: var(--background-color, white);
		width: 100%;
		height: 100%;
	}

	.header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 1rem;
		border-bottom: 1px solid var(--border-color, #eee);
	}

	.header h2 {
		margin: 0;
		font-size: 1.25rem;
		font-weight: 500;
		color: var(--text-color, #333);
	}

	.file-explorer {
		padding: 0.5rem;
	}

	.folder,
	.file {
		padding: 0.5rem;
		margin: 2px 0;
		border-radius: 4px;
		display: flex;
		align-items: center;
		cursor: pointer;
		font-size: 0.9rem;
	}

	.folder:hover,
	.file:hover {
		background-color: var(--hover-color, #f5f5f5);
	}

	.indented {
		margin-left: 1.5rem;
	}

	.icon {
		margin-right: 0.5rem;
		opacity: 0.7;
	}

	.name {
		flex-grow: 1;
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
	}

	.details {
		display: flex;
		gap: 1rem;
		color: var(--text-secondary-color, #666);
		font-size: 0.8rem;
	}

	.folder-header {
		display: flex;
		align-items: center;
		font-weight: 500;
		width: 100%;
	}

	:global(.dark) .file-container {
		--background-color: #1a1b1e;
		--text-color: #e5e5e5;
		--text-secondary-color: #a0a0a0;
		--border-color: #2a2b2e;
		--hover-color: #2a2b2e;
	}
</style>
